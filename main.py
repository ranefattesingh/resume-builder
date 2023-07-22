import json
import os
from builders.resume_builder import ResumeBuilder
from constants.globals import INPUT_DIR_NAME
from decoding.decode_json import decode_json


if __name__ == "__main__":
    files = os.listdir(INPUT_DIR_NAME)
    json = decode_json(INPUT_DIR_NAME, files[0])
    resume = ResumeBuilder(json).add_header().add_educations().add_internships().add_work_experience().add_projects().build()

    print(resume)