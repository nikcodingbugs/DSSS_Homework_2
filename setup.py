from setuptools import setup

setup(
    name="math_quiz",
    version="0.1",
    entry_points={
        "console_scripts": [
            "math_quiz = math_quiz.math_quiz:math_quiz"
        ]
    }
)