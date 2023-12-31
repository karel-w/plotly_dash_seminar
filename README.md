# Dash tutorial for HDS-LEE retreat.

## Clone the git repository.

Make sure  you have git installed on your machine. Lets start by cloning the repository.

1. Open a terminal or command prompt on your local machine.
2. Change to the directory where you want to store the repository (if necessary).
3. Run the following command to clone the repository:
  
```
git clone git@github.com:karel-w/plotly_dash_seminar.git
```

## Setup your environment using Miniconda.

Obtain miniconda from [here](https://docs.conda.io/en/latest/miniconda.html#installing).
Follow miniconda installation instructions from [here](https://conda.io/projects/conda/en/stable/user-guide/install/index.html).

Lets create a conda environment and install the required packages.

```
conda env create --file environment.yml
conda activate dash_tutorial
```

Alternatively you can create the environment from scratch and activate it.
Any python >=3.7 should be sufficient

```
conda create --name dash_tutorial python=3.10
conda activate dash_tutorial
```

Install required packages

```
pip install dash
pip install pandas
pip install dash-bootstrap-components
pip install dash-mantine-components
```

## Generate the mock data.

Change to the data director and run generate_data.py with python.

```
cd data/
python generate_data.py 100000
```

## Test the dashboard.

Change back to the source directory and run the application.py file.

```
cd ../
python src/application.py
```

The application should automatically in your browser. If the browser doesn't open the page, navigate to [localhost:8050](localhost:8050)

