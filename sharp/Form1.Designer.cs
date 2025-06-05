using System.Drawing;
using System.Globalization;
using System.Windows.Forms;

namespace WindowsFormsApp1
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.btnAnonymize = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.txtInputPath = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.button2 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.txtOutputPath = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.txtInfo = new System.Windows.Forms.TextBox();
            this.button4 = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // btnAnonymize
            // 
            this.btnAnonymize.Location = new System.Drawing.Point(464, 186);
            this.btnAnonymize.Name = "btnAnonymize";
            this.btnAnonymize.Size = new System.Drawing.Size(73, 20);
            this.btnAnonymize.TabIndex = 0;
            this.btnAnonymize.Text = "Anonymize";
            this.btnAnonymize.UseVisualStyleBackColor = true;
            this.btnAnonymize.Click += new System.EventHandler(this.btnAnonymize_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(19, 54);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(58, 13);
            this.label1.TabIndex = 1;
            this.label1.Text = "Input path:";
            // 
            // txtInputPath
            // 
            this.txtInputPath.Location = new System.Drawing.Point(19, 69);
            this.txtInputPath.Name = "txtInputPath";
            this.txtInputPath.Size = new System.Drawing.Size(380, 20);
            this.txtInputPath.TabIndex = 2;
            this.txtInputPath.TextChanged += new System.EventHandler(this.txtInputPath_TextChanged);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(169, 28);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(108, 13);
            this.label2.TabIndex = 3;
            this.label2.Text = "Select file or directory";
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(404, 69);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(64, 20);
            this.button2.TabIndex = 4;
            this.button2.Text = "File";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.btnSelectFile_Click);
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(404, 120);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(64, 20);
            this.button3.TabIndex = 6;
            this.button3.Text = "Browse";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.btnSelectOutput_Click);
            // 
            // txtOutputPath
            // 
            this.txtOutputPath.Location = new System.Drawing.Point(19, 120);
            this.txtOutputPath.Name = "txtOutputPath";
            this.txtOutputPath.Size = new System.Drawing.Size(380, 20);
            this.txtOutputPath.TabIndex = 5;
            this.txtOutputPath.TextChanged += new System.EventHandler(this.txtInputPath_TextChanged);
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(19, 104);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(66, 13);
            this.label3.TabIndex = 7;
            this.label3.Text = "Output path:";
            // 
            // txtInfo
            // 
            this.txtInfo.Enabled = false;
            this.txtInfo.Location = new System.Drawing.Point(19, 160);
            this.txtInfo.Name = "txtInfo";
            this.txtInfo.Size = new System.Drawing.Size(518, 20);
            this.txtInfo.TabIndex = 8;
            // 
            // button4
            // 
            this.button4.Location = new System.Drawing.Point(473, 69);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(64, 20);
            this.button4.TabIndex = 9;
            this.button4.Text = "Directory";
            this.button4.UseVisualStyleBackColor = true;
            this.button4.Click += new System.EventHandler(this.btnSelectFolder_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(547, 217);
            this.Controls.Add(this.button4);
            this.Controls.Add(this.txtInfo);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.txtOutputPath);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.txtInputPath);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.btnAnonymize);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private Button btnAnonymize;
        private Label label1;
        private TextBox txtInputPath;
        private Label label2;
        private Button button2;
        private Button button3;
        private TextBox txtOutputPath;
        private Label label3;
        private TextBox txtInfo;
        private Button button4;
    }
}

