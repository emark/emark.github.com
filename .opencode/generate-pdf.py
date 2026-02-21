import os
import markdown
import weasyprint

base_path = os.path.dirname(os.path.abspath(__file__))

with open('resume.md', 'r') as f:
    md_content = f.read()

html_content = markdown.markdown(md_content, extensions=['extra', 'tables'])

qr_image_path = os.path.join(base_path, 'media', 'qr.png')

full_html = f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        @page {{
            margin: 2cm;
            size: A4;
        }}
        body {{
            font-family: Arial, sans-serif;
            font-size: 12pt;
            line-height: 1.5;
        }}
        h1 {{
            font-size: 24pt;
            color: #333;
            margin-bottom: 5pt;
        }}
        h2 {{
            font-size: 16pt;
            color: #555;
            border-bottom: 1px solid #ccc;
            padding-bottom: 5pt;
            margin-top: 20pt;
        }}
        pre {{
            background-color: #f5f5f5;
            padding: 10pt;
            border-radius: 5pt;
            font-size: 10pt;
            overflow-x: auto;
        }}
        a {{
            color: #0066cc;
        }}
        .qr-code {{
            float: right;
            width: 2cm;
            height: 2cm;
            margin: 0 0 1cm 1cm;
        }}
    </style>
</head>
<body>
    <img src="file://{qr_image_path}" alt="QR Code" class="qr-code" />
    {html_content}
</body>
</html>
'''

weasyprint.HTML(string=full_html, base_url=base_path).write_pdf('resume.pdf')
print('PDF created: resume.pdf')
