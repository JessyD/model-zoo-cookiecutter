# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import json
import pandas as pd
import numpy as np
from bids.modeling import BIDSStatsModelsGraph
from bids.layout import BIDSLayout
from pathlib import Path
from nilearn.plotting import plot_design_matrix

# %% [markdown]
# # {{cookiecutter.example_name}}

# %% [markdown]
# #### Set Up
# Instantiate the `BIDSLayout` to index the dataset, and load `BIDS Stats Model` JSON document
# Define variables from the information passed to cookiecutter
dataset_path = {{cookiecutter.dataset_path}}
example_name = {{cookiecutter.example_name}}

# %%
layout = BIDSLayout(f'./{{cookiecutter.dataset_path}}/', derivatives=f'./{{cookiecutter.dataset_path}}/derivatives/fmriprep/')

# %% [markdown]
# #### Model & model graph

# %%
model_json = f'model-{example_name}_smdl.json'
spec = model_json.loads(Path(json_file).read_text())
spec

# %%
graph = BIDSStatsModelsGraph(layout, spec)

# %%
graph.write_graph(format='svg')

# %% [markdown]
# First, let's load collections of variables from the Dataset for the entire Graph

# %%
try:
    graph.load_collections()
except ValueError:
    scan_length=453 # Set scan length to avoid downloadin images
    graph.load_collections(scan_length=453) 

# %% [markdown]
# #### Run-level node
#
# Let's look at the run-level node

# %%
specs = graph.root_node.run()
len(specs)

# %%
# Design matrix for first run
specs[0].X

# %%
plot_design_matrix(specs[0].X)

# %%
specs[0].entities

# %%
specs[0].metadata

# %%
next_node = root_node.children[0].destination

# %%
next_node.group_by
