from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig


engine = AnonymizerEngine()

result = engine.anonymize(
    text="My name is Long Le",
    analyzer_results=[
        RecognizerResult(entity_type="PERSON", start=11, end=19, score=0.9),
    ],
    operators={"PERSON": OperatorConfig("replace", {"new_value": "LongNguyenThanhLe"})},
)

print(result)
