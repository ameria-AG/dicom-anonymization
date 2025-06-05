using System;
using System.IO;
using System.Security.Cryptography;
using System.Windows.Forms;
using static System.Net.WebRequestMethods;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            txtInputPath.Text = Environment.CurrentDirectory;
            txtOutputPath.Text = Path.Combine(Environment.CurrentDirectory, "Output");

            ImageHelper.SupressItkWarning();
        }

        private void btnSelectOutput_Click(object sender, EventArgs e)
        {
            using (FolderBrowserDialog openFolderDialog = new FolderBrowserDialog())
            {
                //openFolderDialog.RootFolder = Environment.SpecialFolder.MyComputer;
                openFolderDialog.SelectedPath = Environment.CurrentDirectory;
                if (openFolderDialog.ShowDialog() == DialogResult.OK)
                {
                    txtOutputPath.Text = openFolderDialog.SelectedPath;
                }
            }
        }

        private void btnSelectFile_Click(object sender, EventArgs e)
        {
            using (OpenFileDialog openFileDialog = new OpenFileDialog())
            {
                openFileDialog.InitialDirectory = Environment.CurrentDirectory;
                openFileDialog.Filter = "DCM files (*.dcm)|*.dcm";
                openFileDialog.FilterIndex = 1;
                openFileDialog.RestoreDirectory = true;

                if (openFileDialog.ShowDialog() == DialogResult.OK)
                {
                    txtInputPath.Text = openFileDialog.FileName;
                }
            }
        }

        private void btnSelectFolder_Click(object sender, EventArgs e)
        {
            using (FolderBrowserDialog openFolderDialog = new FolderBrowserDialog())
            {
                //openFolderDialog.RootFolder = Environment.SpecialFolder.MyComputer;
                openFolderDialog.SelectedPath = Environment.CurrentDirectory;
                if (openFolderDialog.ShowDialog() == DialogResult.OK)
                {
                    txtInputPath.Text = openFolderDialog.SelectedPath;
                }
            }
        }

        private void CheckPathes()
        {
            if (System.IO.File.Exists(txtInputPath.Text))
            {
                var extension = Path.GetExtension(txtInputPath.Text).ToLower();
                if (!extension.EndsWith(".dcm"))
                {
                    btnAnonymize.Enabled = false;
                    txtInfo.Text = "Input file is not .dcm";
                    return;
                }
            }
            else if (!Directory.Exists(txtInputPath.Text))
            {
                btnAnonymize.Enabled = false;
                txtInfo.Text = "Input path is not valid";
                return;
            }

            if (Directory.Exists(txtOutputPath.Text))
            {
                var normInputPath = Path.GetFullPath(txtInputPath.Text);
                var normOutputPath = Path.GetFullPath(txtOutputPath.Text);
                if (normOutputPath.StartsWith(normInputPath))
                {
                    btnAnonymize.Enabled = false;
                    txtInfo.Text = "Output path can't be inside of input path";
                    return;
                }

                btnAnonymize.Enabled = true;
                txtInfo.Text = "Click 'Anonymize' button to start";
            }
            else
            {
                btnAnonymize.Enabled = false;
                txtInfo.Text = "Output path is not valid";
            }
        }

        private void txtInputPath_TextChanged(object sender, EventArgs e)
        {
            CheckPathes();
        }

        private void btnAnonymize_Click(object sender, EventArgs e)
        {
            if (System.IO.File.Exists(txtInputPath.Text))
            {
                string outputFile = Path.Combine(txtOutputPath.Text, Path.GetFileName(txtInputPath.Text));
                ImageHelper.MakeAnonimAndSaveFile(txtInputPath.Text, outputFile);
                txtInfo.Text = "File saved to " + outputFile;
            }
            else if (Directory.Exists(txtInputPath.Text))
            {
                var filesCount = ImageHelper.AnonymizeDir(txtInputPath.Text, txtOutputPath.Text);
                txtInfo.Text = filesCount.ToString() + " files saved to " + txtOutputPath.Text;
            }
        }
    }
}
