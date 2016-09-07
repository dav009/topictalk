# Instructions

1. Install Docker: https://docs.docker.com/engine/installation/

2. Clone this repo: `git clone https://github.com/dav009/topictalk`

2. Do `docker pull dav009/python3-topic-tutorial`

3. Do `docker run -d -p 8889:8888 -v PATH_TO_CLONE_REPO:/home/ds/notebooks dav009/python3-topic-tutorial`

 - replace `PATH_TO_CLONE_REPO` with the path to `topictalk` repo

4. Open `http://localhost:8889/notebooks/Tutorial.ipynb`