import hashlib
import SimpleITK as sitk
import dicom_tags
import datetime


def sanitize_utf8(v: str) -> str:
    try:
        return v.encode("utf-8", errors="replace").decode("utf-8")
    except Exception:
        return "ANONYMIZED"

class TagAnonymizer:
    def __init__(self, salt="ameria_salt"):
        self.salt = salt.encode("utf-8")
        self.value_map = {}


    def _hash_string(self, value: str, prefix="anon") -> str:
        if value in self.value_map:
            return self.value_map[value]
        sha = hashlib.sha256(self.salt + value.encode()).hexdigest()
        anon = f"{prefix}-{sha[:10]}"
        self.value_map[value] = anon
        return anon

    def _uid_from_hash(self, value: str) -> str:
        """Create a valid DICOM UID from a hashed value."""
        if value in self.value_map:
            return self.value_map[value]
        sha = hashlib.sha256(self.salt + value.encode()).digest()
        base_int = int.from_bytes(sha[:16], byteorder="big")
        uid = f"2.25.{base_int}"
        self.value_map[value] = uid
        return uid

    def _generate_fake_date(self, value: str) -> str:
        """Generate a consistent fake date in YYYYMMDD format."""
        sha = hashlib.sha256(self.salt + value.encode()).digest()
        days_offset = int.from_bytes(sha[:2], byteorder="big") % 20000  # ~55 years range
        base_date = datetime.date(1950, 1, 1)
        fake_date = base_date + datetime.timedelta(days=days_offset)
        return fake_date.strftime("%Y%m%d")

    def _generate_fake_time(self, value: str) -> str:
        """Generate a consistent fake time in HHMMSS format."""
        sha = hashlib.sha256(self.salt + value.encode()).digest()
        seconds = int.from_bytes(sha[2:4], byteorder="big") % 86400  # seconds in a day
        h = seconds // 3600
        m = (seconds % 3600) // 60
        s = seconds % 60
        return f"{h:02}{m:02}{s:02}"


    def anonymize_image(self, image: sitk.Image) -> sitk.Image:
        """Return a copy of the image with anonymized metadata."""
        anon_img = sitk.Image(image)  # clone image
        for key in image.GetMetaDataKeys():
            value = sanitize_utf8(image.GetMetaData(key))
            anon_value = value
            try:
                if key.upper() in dicom_tags.SENSITIVE_TAGS_DATE:
                    anon_value = self._generate_fake_date(value)
                elif key.upper() in dicom_tags.SENSITIVE_TAGS_TIME:
                    anon_value = self._generate_fake_time(value)
                elif key.upper() in dicom_tags.SENSITIVE_TAGS_UID:
                    anon_value = self._uid_from_hash(value)
                elif key.upper() in dicom_tags.SENSITIVE_TAGS_UINT:
                    anon_value = "0000"  # or some hashed placeholder
                elif key.upper() in dicom_tags.SENSITIVE_TAGS_STRING:
                    anon_value = self._hash_string(value)
                elif key.upper() in dicom_tags.SENSITIVE_TAGS_OTHER:
                    anon_value = ""  # or erase/skip it

                anon_img.SetMetaData(key, sanitize_utf8(anon_value))
            except Exception as e:
                print(f"Error anonymizing tag {key}: {e}")
                print("Original value:", value)
                print("Anonymized value:", anon_value)
                raise e

        return anon_img