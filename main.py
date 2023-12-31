import json
import os
import sys

from builders.resume_builder import ResumeBuilder
from document.build import create_with_default_template
from constants.globals import INPUT_DIR_NAME
from decoding.decode_json import decode_json


if __name__ == "__main__":
    dynamic_files = sys.argv[1:]
    files = os.listdir(INPUT_DIR_NAME)
   
    for file_name in files:
        json = decode_json(INPUT_DIR_NAME, file_name)
        resume = ResumeBuilder(json).add_header().add_educations().add_internships().add_work_experience().add_projects().add_skillset().add_achievements().add_interests().add_hobbies().add_languages().build()

        create_with_default_template(resume)

    print("Task completed!")