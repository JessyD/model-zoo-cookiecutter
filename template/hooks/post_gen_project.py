import subprocess

subprocess.call(f'datalad install {{cookiecutter.dataset_url}}', shell=True)
