from models.duration import Duration


class Education:
    degree      : str
    institute   : str
    branch      : str
    score       : str
    duration    : Duration

    def __init__(self, degree : str, institute : str, branch : str, score : str, duration: Duration) -> None:
        self.degree = degree
        self.institute = institute
        self.branch = branch
        self.score = score
        self.duration = duration