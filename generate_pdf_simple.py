from fpdf import FPDF

class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Cat Distribution System Inc.', 0, 1, 'C')
        self.set_font('Arial', 'I', 10)
        self.cell(0, 10, 'AR Mobile Game Project Report', 0, 1, 'C')
        self.ln(5)
    
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

pdf = PDFReport()
pdf.add_page()

# Metadata
pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 8, 'Authors:', 0, 1)
pdf.set_font('Arial', '', 11)
pdf.cell(0, 6, 'Monika Szuban, Vanessa Scherer, Hannah Muller', 0, 1)
pdf.ln(3)

pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 8, 'Institution:', 0, 1)
pdf.set_font('Arial', '', 11)
pdf.cell(0, 6, 'Technische Hochschule Ingolstadt', 0, 1)
pdf.ln(3)

pdf.set_font('Arial', 'B', 11)
pdf.cell(0, 8, 'Subject:', 0, 1)
pdf.set_font('Arial', '', 11)
pdf.cell(0, 6, 'Augmented and Virtual Reality Applications', 0, 1)
pdf.ln(8)

# Problem Statement
pdf.set_font('Arial', 'B', 14)
pdf.cell(0, 10, 'Problem Statement', 0, 1)
pdf.set_font('Arial', '', 11)
pdf.multi_cell(0, 6, 'This project was developed as part of a semester assignment requiring three mini-games: one in 2D and two using AR technology with image recognition, obscured objects, and interactive actions. The challenge was transforming these broad requirements into a cohesive, engaging product.')
pdf.ln(3)
pdf.multi_cell(0, 6, 'Our team decided to frame the project around virtual cat care, blending playfulness with educational elements teaching responsibility in pet ownership. The goal was to create an experience where players could learn about caring for pets while having fun.')
pdf.ln(3)
pdf.multi_cell(0, 6, 'We named it Cat Distribution System Inc., inspired by the idea that "cats adopt us, not the other way around." The concept balanced humor with purpose, giving the game both character and educational direction.')
pdf.ln(5)

# Method
pdf.set_font('Arial', 'B', 14)
pdf.cell(0, 10, 'Method', 0, 1)
pdf.set_font('Arial', '', 11)
pdf.multi_cell(0, 6, 'We structured the game around three distinct mini-games connected by theme. Development used Unity and AR Foundation, with Figma for UI design and Blender for 3D assets. Agile sprints and two rounds of usability testing shaped the final experience through iterative improvement.')
pdf.ln(3)

pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 8, 'Three Mini-Games', 0, 1)
pdf.set_font('Arial', '', 11)
pdf.multi_cell(0, 6, '- Memory Game (2D): Classical matching of cat-related items under time and move limits.\n- Toy Hunt (AR): Scan environment to find hidden boxes containing cat toys with interactive feedback.\n- Flappy Cat (AR): Tilt-controlled obstacle avoidance game featuring the virtual cat.')
pdf.ln(3)

pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 8, 'Testing & Iteration', 0, 1)
pdf.set_font('Arial', '', 11)
pdf.multi_cell(0, 6, 'After the first usability round, we identified struggles with AR onboarding and progress visibility. We responded with tutorials, help overlays, and progress counters. By the second round, HARUS scores improved significantly.')
pdf.ln(3)

pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 8, 'Tools Used', 0, 1)
pdf.set_font('Arial', '', 11)
pdf.multi_cell(0, 6, 'Unity & AR Foundation for development, Figma for UI design, Blender for 3D models, and AI tools (ChatGPT, Claude) for rapid prototyping and debugging support.')
pdf.ln(5)

# Outcomes
pdf.set_font('Arial', 'B', 14)
pdf.cell(0, 10, 'Outcomes', 0, 1)
pdf.set_font('Arial', '', 11)
pdf.multi_cell(0, 6, 'The final game featured three fully integrated mini-games with measurably improved usability between test rounds. We made the game available on GitHub and were invited to showcase it at GG Bavaria Convention (March 2025), validating its educational and entertainment value.')
pdf.ln(3)

pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 8, 'Key Achievements', 0, 1)
pdf.set_font('Arial', '', 11)
pdf.multi_cell(0, 6, '- Functional AR Integration: Successfully implemented image recognition, object tracking, and interactive AR experiences across two mini-games.\n- Improved Usability: HARUS survey scores showed significant improvement in onboarding clarity and progress tracking between testing rounds.\n- Educational Impact: Balanced playful design with subtle lessons on pet care responsibility, achieving the project\'s dual purpose.\n- External Recognition: Selected for showcase at GG Bavaria Convention, demonstrating the game\'s polish and appeal beyond the classroom.')
pdf.ln(3)

pdf.multi_cell(0, 6, 'The project received top marks in the Augmented and Virtual Reality Applications course and is available on GitHub for download.')

pdf.output('assets/projects/CDSInc_Project_Report.pdf')
print("PDF created successfully!")
