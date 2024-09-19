import pandas as pd
import os
from unittest import mock
from main import main


def test_main_plot():
    # Sample DataFrame
    df_sample = pd.DataFrame(
        {
            "Valuation": ["$1B", "$2B", "$500M", "$1.5B"],
            "Funding": ["$500M", "$1B", "$250M", "$750M"],
            "Industry": ["Tech", "Health", "Finance", "Tech"],
        }
    )

    funding_values = [0.5e9, 1e9, 0.25e9, 0.75e9]
    valuation_values = [1e9, 2e9, 0.5e9, 1.5e9]
    value_creation = [
        (val - fund) / 1e9 for val, fund in zip(valuation_values, funding_values)
    ]

    # Statistics
    expected_stats = pd.Series(value_creation).agg(["std", "mean", "median"])

    with mock.patch("lib.dataset_import", return_value=df_sample), mock.patch(
        "lib.data_modeling", return_value=df_sample
    ), mock.patch("main.plot_value_creation_by_industry") as mock_plot:

        main()  # Call the main function
        mock_plot.assert_called_once()  # Check if the plot function was called

        # Check if the plot was saved to the expected path
        expected_save_dir = (
            r"C:/Users/chris/Downloads/IDS706/chris_moriera_valuecreation_pandas/"
        )
        assert os.path.exists(expected_save_dir)


if __name__ == "__main__":
    test_main_plot()
