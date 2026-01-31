# Arty - Art Curator AI Agent

🚧 On construction 🚧

## Setup

- Install conda environment
    ``` 
    $ conda env create -f env.yaml
    $ conda activate arty
    ```
- Create **config/local.yaml** and save your OpenAI LLM API Key like below.
    ```
    openai:
        api_key: YOUR_API_KEY
        base_url: BASE_URL
    ```
- (Optional) Go to **notebooks/graph_viz.ipynb** and check the workflow.
- run a test script in **scripts/run_test.sh**

    ```
    $ bash scripts/run_test.sh
    ```
    It creates a sample report named **final_report.md**

