import unittest
from app.models.workflow import WorkflowItem
from pydantic import ValidationError

class TestWorkflowItem(unittest.TestCase):
    
    def test_workflow_item_validation(self):
        valid_data = {
            "id": "1234",
            "project": 1,
            "team": "team-A",
            "ts_start": 1635689661,
            "duration": 200,
            "runner_id": 2,
            "name": "Build",
            "success": 1
        }
        
        item = WorkflowItem(**valid_data)
        self.assertEqual(item.id, valid_data["id"])
        
        with self.assertRaises(ValidationError):
            WorkflowItem(**{**valid_data, "success": 3})  # Invalid success value

if __name__ == "__main__":
    unittest.main()