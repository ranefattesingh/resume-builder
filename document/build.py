import os
from docx.shared import Pt, RGBColor
from constants.globals import DEFAULT_TEMPLATE_FILE_NAME, TEMPLATE_DIR_NAME, TEMPLATE_OUTPUT_DIR_NAME
from docx import Document

from models.resume import Resume

def create_with_default_template(resume: Resume):
    document = Document(os.path.join(TEMPLATE_DIR_NAME, DEFAULT_TEMPLATE_FILE_NAME))

    document.paragraphs[0].runs[0].text = resume.header.intro

    # header table
    header_container_table = document.tables[0]
    header_table = header_container_table.cell(0, 0).tables[0]
    
    # name table
    header_table.cell(0, 0).text = resume.header.name.upper()
    header_table.cell(0, 0).paragraphs[0].runs[0].font.size = Pt(30)

    # detail table
    detail_table = header_table.cell(0, 1).tables[0]
    for rowIndex in range(0, len(detail_table.rows)):
        key = detail_table.rows[rowIndex].cells[1].text
        print(key)
        detail_items = list(filter(lambda detail: detail.field_icon == key, resume.header.details))
        value = ''
        if len(detail_items) == 1:
            value = detail_items[0].field_value
        detail_table.rows[rowIndex].cells[1].text = value

    contentTable = document.tables[1]

    # Academic Profile
    add_academic_profile(resume.educations, contentTable.cell(0, 1).tables[0])
    add_experience(resume.internships, contentTable.cell(2, 1).tables[0])
    add_experience(resume.work_experiences, contentTable.cell(4, 1).tables[0])
    

    
    document.save(os.path.join(TEMPLATE_OUTPUT_DIR_NAME, resume.header.name + ' Resume' + ".docx"))


def add_academic_profile(educations, academic_profile_table):
    for row in academic_profile_table.rows:
        remove_row(academic_profile_table, row)
    
    
    for education in educations:
        academic_profile_table.add_row()
        academic_profile_table.rows[len(academic_profile_table.rows)-1].cells[0].text = education.institute
        academic_profile_table.rows[len(academic_profile_table.rows)-1].cells[0].paragraphs[0].runs[0].bold = True
        academic_profile_table.rows[len(academic_profile_table.rows)-1].cells[0].paragraphs[0].runs[0].underline  = True
        academic_profile_table.rows[len(academic_profile_table.rows)-1].cells[0].paragraphs[0].runs[0].font.size  = Pt(11)

        academic_profile_table.add_row()
        academic_profile_table.rows[len(academic_profile_table.rows)-1].cells[0].text = education.degree

        if education.branch != "":
            academic_profile_table.add_row()
            academic_profile_table.rows[len(academic_profile_table.rows)-1].cells[0].text = education.branch
        
        academic_profile_table.add_row()
        if education.duration.from_date != '':
            academic_profile_table.rows[len(academic_profile_table.rows)-1].cells[0].text = education.duration.from_date + " - " + education.duration.to_date
        else:
            academic_profile_table.rows[len(academic_profile_table.rows)-1].cells[0].text = education.duration.to_date

        academic_profile_table.rows[len(academic_profile_table.rows)-1].cells[0].paragraphs[0].runs[0].bold = True
        academic_profile_table.rows[len(academic_profile_table.rows)-1].cells[0].paragraphs[0].runs[0].font.color.rgb = RGBColor(0x80, 0x80, 0x80)

        if education.duration.duration != '':
            academic_profile_table.add_row()
            academic_profile_table.rows[len(academic_profile_table.rows)-1].cells[0].text = education.duration.duration

        
        academic_profile_table.add_row()
        academic_profile_table.rows[len(academic_profile_table.rows)-1].cells[0].text = education.score
        academic_profile_table.rows[len(academic_profile_table.rows)-1].cells[0].paragraphs[0].runs[0].bold = True
        academic_profile_table.add_row()

    remove_row(academic_profile_table, academic_profile_table.rows[len(academic_profile_table.rows)-1])

def add_experience(experiences, experience_table):
    for row in experience_table.rows:
        remove_row(experience_table, row)

    for experience in experiences:
        experience_table.add_row()
        experience_table.rows[len(experience_table.rows)-1].cells[0].text = experience.organization
        experience_table.rows[len(experience_table.rows)-1].cells[0].paragraphs[0].runs[0].bold = True
        experience_table.rows[len(experience_table.rows)-1].cells[0].paragraphs[0].runs[0].underline  = True
        experience_table.rows[len(experience_table.rows)-1].cells[0].paragraphs[0].runs[0].font.size  = Pt(11)

        experience_table.add_row()
        experience_table.rows[len(experience_table.rows)-1].cells[0].text = experience.title

        if len(experience.description) > 0:
            for description in experience.description:
                experience_table.add_row()
                experience_table.rows[len(experience_table.rows)-1].cells[0].text = ('   •   ' + description)
                # delete_paragraph(experience_table.rows[len(experience_table.rows)-1].cells[0].paragraphs[0])
                experience_table.rows[len(experience_table.rows)-1].cells[0].paragraphs[0].runs[0].bold = True
                experience_table.rows[len(experience_table.rows)-1].cells[0].paragraphs[0].runs[0].font.size  = Pt(9)

        if len(experience.tech_stack) > 0:
            experience_table.rows[len(experience_table.rows)-1].cells[0].text = ', '.join(experience.tech_stack)
        
        experience_table.add_row()
        if experience.duration.from_date != '':
            experience_table.rows[len(experience_table.rows)-1].cells[0].text = experience.duration.from_date + " - " + experience.duration.to_date
        else:
            experience_table.rows[len(experience_table.rows)-1].cells[0].text = experience.duration.to_date

        experience_table.rows[len(experience_table.rows)-1].cells[0].paragraphs[0].runs[0].bold = True
        experience_table.rows[len(experience_table.rows)-1].cells[0].paragraphs[0].runs[0].font.color.rgb = RGBColor(0x80, 0x80, 0x80)

        if experience.duration.duration != '':
            experience_table.add_row()
            experience_table.rows[len(experience_table.rows)-1].cells[0].text = experience.duration.duration
            experience_table.rows[len(experience_table.rows)-1].cells[0].paragraphs[0].runs[0].bold = True

        experience_table.add_row()

    remove_row(experience_table, experience_table.rows[len(experience_table.rows)-1])


def remove_row(table, row):
    tbl = table._tbl
    tr = row._tr
    tbl.remove(tr)

def delete_paragraph(paragraph):
    p = paragraph._element
    p.getparent().remove(p)
    p._p = p._element = None
