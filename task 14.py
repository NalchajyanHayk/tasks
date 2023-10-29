from abc import ABC, abstractmethod
from validations import Validations

# Define the abstract class for job search operations
class JobSearch(ABC):
    @abstractmethod
    def search_jobs(self, keyword):
        pass

    @abstractmethod
    def apply(self, job_posting):
        pass

# Interface for different types of job postings
class FullTimeJob(ABC):
    @abstractmethod
    def is_full_time(self):
        pass

class PartTimeJob(ABC):
    @abstractmethod
    def is_part_time(self):
        pass

# Define the Company class
class Company:
    def __init__(self, name, contact_info):
        self._name = name
        self._contact_info = contact_info
        self._job_postings = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if Validations.is_valid_name(value):
            self._name = value
        else:
            print("invalid input")

    @property
    def contact_info(self):
        return self._contact_info

    @contact_info.setter
    def contact_info(self, value):
        if Validations.is_valid_email(value):
            self._contact_info = value
        else:
            print("invalid contact info, it should be an email")

    @property
    def job_postings(self):
        return self._job_postings

    @job_postings.setter
    def job_postings(self, value):
        self._job_postings = value

    def post_job(self, title, description, salary):
        job_posting = JobPosting(title, description, salary, self)
        self._job_postings.append(job_posting)
        return job_posting

    def review_applications(self, job_posting):
        print(f"Reviewing applications for {job_posting.title}")

# Define the JobPosting class
class JobPosting(FullTimeJob, PartTimeJob):
    def __init__(self, title, description, salary, company):
        self._title = title
        self._description = description
        self._salary = salary
        self._company = company

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if Validations.is_valid_name(value):
            self._title = value
        else:
            print("invalid value")

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if Validations.has_more_than_10_words(value):
            self._description = value
        else:
            print("invalid description")

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if type(value) == eval and value > 0:
            self._salary = value
        else:
            print("invalid Value")

    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, value):
        if type(value) == Company:
            self._company = value
        else:
            print("invalid input")

    def is_full_time(self):
        return "full-time" in self._title.lower()

    def is_part_time(self):
        return "part-time" in self._title.lower()

# Define the JobSeeker class
class JobSeeker(JobSearch):
    def __init__(self, name, contact_info):
        self._name = name
        self._contact_info = contact_info
        self._resume = ""

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if Validations.is_valid_name(value):
            self._name = value
        else:
            print("invalid name")

    @property
    def contact_info(self):
        return self._contact_info

    @contact_info.setter
    def contact_info(self, value):
        if Validations.is_valid_email(value):
            self._contact_info = value
        else:
            print("invalid contact info")

    @property
    def resume(self):
        return self._resume

    @resume.setter
    def resume(self, value):
        if Validations.has_more_than_10_words(value):
            self._resume = value
        else:
            print("invalid resume")

    def update_resume(self, resume):
        if Validations.has_more_than_10_words(resume):
            self._resume = resume
        else:
            print("invalid input")

    def search_jobs(self, keyword):

        matching_jobs = [job for job in all_job_postings if keyword.lower() in job.title.lower()]
        return matching_jobs

    def apply(self, job_posting):
        if type(job_posting) == JobPosting:
            print(f"Applying for {job_posting.title} at {job_posting.company.name}")
        else:
            print("invalid job posting")

# Sample data
company1 = Company("TechCorp", "contact@techcorp.com")
company2 = Company("HealthTech", "contact@healthtech.com")

job_posting1 = company1.post_job("Full-Time Software Engineer", "Develop software applications", 80000)
job_posting2 = company2.post_job("Part-Time Data Analyst", "Analyze data and generate insights", 60000)

all_job_postings = [job_posting1, job_posting2]

job_seeker1 = JobSeeker("Alice", "alice@email.com")
job_seeker2 = JobSeeker("Bob", "bob@email.com")
job_seeker1.update_resume("Alice's Resume: Skills, Experience, etc.")

# Job seekers searching and applying for jobs
matching_jobs = job_seeker1.search_jobs("Software")
for job in matching_jobs:
    job_seeker1.apply(job)

# Companies reviewing applications
for posting in company1.job_postings:
    company1.review_applications(posting)
