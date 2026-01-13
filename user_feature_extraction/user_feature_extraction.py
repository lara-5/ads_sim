import marimo

__generated_with = "0.19.2"
app = marimo.App()


@app.cell
def _():
    import pandas as pd
    import requests
    import marimo as mo
    import matplotlib.pyplot as plt
    import seaborn as sns
    from io import StringIO
    return StringIO, mo, pd, plt, requests, sns


@app.cell
def __(requests):
    # 1. Extract features from dataset
    # Fetch data using Zendo endpoint
    zenodo_api_url = "https://zenodo.org/api/records/3541657"
    response = requests.get(zenodo_api_url)
    record_data = response.json()

    # Extract file download links
    file_links = {file["key"]: file["links"]["self"] for file in record_data["files"]}
    return file_links, record_data, response, zenodo_api_url


@app.cell
def __(StringIO, file_links, pd, requests):
    # Download and load data
    dataset_url = file_links["dataset.csv"]
    documentation_url = file_links["documentation.csv"]

    dataset_response = requests.get(dataset_url)
    documentation_response = requests.get(documentation_url)

    dataset_csv = StringIO(dataset_response.text)
    documentation_csv = StringIO(documentation_response.text)

    df = pd.read_csv(dataset_csv)
    doc_df = pd.read_csv(documentation_csv)
    return (
        dataset_csv,
        dataset_response,
        dataset_url,
        df,
        doc_df,
        documentation_csv,
        documentation_response,
        documentation_url,
    )


@app.cell
def __(df, doc_df):
    # Create a dataframe that assigns each row with user_id and combines features
    # Feature descriptions are in the documentation dataframe
    feature_descriptions = doc_df[doc_df["variable"].isin(df.columns)]
    
    # For simplicity, we'll use the original dataframe and assume each row is a user
    df_processed = df.copy()
    df_processed["user_id"] = df_processed.index
    return df_processed, feature_descriptions


@app.cell
def __(df_processed, mo):
    # 2. EDA analysis
    # Remove any missing rows
    df_processed = df_processed.dropna()
    
    # Display some basic info
    eda_section = mo.md(
        f"""
        ## Exploratory Data Analysis
        
        ### Data Shape
        {df_processed.shape}
        
        ### Data Info
        {df_processed.info()}
        
        ### Missing Values
        {df_processed.isnull().sum().sum()}
        """
    )
    return eda_section


@app.cell
def __(df_processed, plt, sns):
    # Visualize distributions and correlations
    fig, axes = plt.subplots(3, 2, figsize=(15, 15))
    sns.histplot(df_processed["age"], kde=True, ax=axes[0, 0])
    axes[0, 0].set_title("Age Distribution")

    sns.countplot(x="gender", data=df_processed, ax=axes[0, 1])
    axes[0, 1].set_title("Gender Distribution")

    sns.histplot(df_processed["openness"], kde=True, ax=axes[1, 0])
    axes[1, 0].set_title("Openness Distribution")

    sns.histplot(df_processed["agreeableness"], kde=True, ax=axes[1, 1])
    axes[1, 1].set_title("Agreeableness Distribution")

    sns.histplot(df_processed["conscientiousness"], kde=True, ax=axes[2, 0])
    axes[2, 0].set_title("Conscientiousness Distribution")

    sns.histplot(df_processed["extraversion"], kde=True, ax=axes[2, 1])
    axes[2, 1].set_title("Extraversion Distribution")

    plt.tight_layout()
    
    return axes, fig


@app.cell
def __(df_processed, plt, sns):
    correlation_matrix = df_processed.corr()
    plt.figure(figsize=(12, 10))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
    plt.title("Correlation Matrix")
    return correlation_matrix


@app.cell
def _():
    # 3. Choose agents
    # For this simulation, we'll select a diverse subset of 1000 agents.
    # A simple approach is to sample randomly.
    # For a more sophisticated approach, one could use clustering
    # to ensure representation from different user profiles.
    return


@app.cell
def __(df_processed):
    agents_df = df_processed.sample(n=1000, random_state=42)
    return (agents_df,)


@app.cell
def __(agents_df):
    # Save dataframe in data/users_features.csv
    agents_df.to_csv("data/users_features.csv", index=False)
    return


if __name__ == "__main__":
    app.run()
