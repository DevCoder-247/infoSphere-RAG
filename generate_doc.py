from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet

# Output PDF name
pdf_path = "DocumentAI_Setup_Guide.pdf"

# Setup document styles
styles = getSampleStyleSheet()
title_style = styles['Heading1']
body_style = styles['BodyText']
body_style.spaceAfter = 10

# Create PDF document
doc = SimpleDocTemplate(pdf_path, pagesize=A4)
content = []

# Title
content.append(Paragraph("DocumentAI - Setup & User Guide", title_style))
content.append(Spacer(1, 12))

# Project Explanation
project_intro = """
<b>Project Overview:</b><br/>
DocumentAI is an AI-powered document processing system built using Python, Flask, LangChain, and Google Generative AI.
It allows users to upload and process documents like PDFs, extract meaningful content, perform text-based queries,
and use AI models to generate summaries or answers from document data.
"""
content.append(Paragraph(project_intro, body_style))

# Features & Future Enhancements
features_text = """
<b>Key Features:</b>
- PDF & Image Document Upload & Processing  
- Text Extraction using PyMuPDF & OCR (pytesseract)  
- AI-Powered Query Processing with LangChain + Google GenAI  
- Vector Search for Efficient Retrieval (FAISS)  
- Web Interface using Gradio  
- Environment Variable Support for API Keys  

<b>Future Enhancements:</b>
- Multi-language Document Processing  
- Integration with OpenAI GPT & Claude  
- Role-based Authentication  
- Real-time Collaboration  
- Export Results to PDF/Word  
- Docker Deployment for Production  
"""
content.append(Paragraph(features_text, body_style))

# Setup Instructions
setup_instructions = """
<b>Setup Instructions:</b><br/>
1. Install Python 3.10+ & VS Code  
2. Open project in VS Code  
3. Create virtual environment: <font color='blue'>python -m venv venv</font>  
4. Activate it: <font color='blue'>venv\\Scripts\\activate</font>  
5. Install dependencies: <font color='blue'>pip install -r requirements.txt</font>  
6. Add API keys in the .env file  
"""
content.append(Paragraph(setup_instructions, body_style))

# Running Instructions
running_instructions = """
<b>Running the Project:</b><br/>
1. Start backend: <font color='blue'>python app.py</font>  
2. Start Gradio UI: <font color='blue'>python gradio_app.py</font>  
3. Open: <font color='green'>http://127.0.0.1:7860</font>  
"""
content.append(Paragraph(running_instructions, body_style))

# Troubleshooting Section
troubleshooting = """
<b>Common Issues:</b><br/>
- Missing Modules: Install with pip  
- Port Already in Use: Change port in gradio_app.py  
- Dependency Conflicts: Update requirements.txt  
"""
content.append(Paragraph(troubleshooting, body_style))

# Dependency Table
dependencies_data = [
    ["Library", "Purpose"],
    ["Flask", "Backend API framework"],
    ["Gradio", "Web interface"],
    ["LangChain", "AI & LLM integration"],
    ["FAISS", "Vector database for embeddings"],
    ["PyMuPDF / pytesseract", "PDF & Image text extraction"],
    ["Sentence Transformers", "Embeddings generation"],
    ["Google Generative AI", "AI model integration"]
]
table = Table(dependencies_data, hAlign='LEFT')
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
]))
content.append(Spacer(1, 12))
content.append(table)

# Build PDF
doc.build(content)
print(f"PDF Generated: {pdf_path}")
