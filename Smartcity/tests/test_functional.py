
import unittest
from jobs import config, main

class TestSmartCityProject(unittest.TestCase):
    def test_config_loading(self):
        """Test if the configuration loads correctly"""
        try:
            config_data = config.load_config()
            self.assertIsNotNone(config_data, "Config should not be None")
        except Exception as e:
            self.fail(f"Config loading failed with error: {e}")

    def test_main_execution(self):
        """Test if the main script runs without errors"""
        try:
            result = main.run()
            self.assertTrue(result, "Main script should execute successfully")
        except Exception as e:
            self.fail(f"Main script execution failed with error: {e}")

    def test_data_processing(self):
        """Test if data processing produces valid results"""
        try:
            processed_data = main.process_data()
            self.assertIsInstance(processed_data, list, "Processed data should be a list")
            self.assertGreater(len(processed_data), 0, "Processed data should not be empty")
        except Exception as e:
            self.fail(f"Data processing failed with error: {e}")

if __name__ == "__main__":
    unittest.main()
