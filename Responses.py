from datetime import datetime


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ('hello', 'hi', 'sup'):
        return "Hey! How's it going?"

    if user_message in ('Who are you', 'who are you?'):
        return "I am Justin's first bot!"

    if user_message in ('time', 'time?'):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)
    if user_message in ('description'):
        return "Provides the knowledge on how to model real life problems by casting them against a rigorous modelling framework on the topics of multivariable calculus and linear algebra. This course builds upon the Term 1 course, Modelling and Analysis, and will cover the following topics: differentiation and integration in multiple dimensions, optimization, line integrals, linear maps, eigenvalues and eigenvectors. By working in group projects and writing MATLAB codes, students will appreciate the various topics and connections between mathematics and physics, computer science, probability, statistics and other topics."

    if user_message in ('lessons'):
        return 'One 60 minutes online lecture; Two 150 minutes cohort classes per week'
    if user_message in ('grading'):
        return 'Grades will be based on homework, 1D project, participation, and exams.'

    return "I don't understand you."
