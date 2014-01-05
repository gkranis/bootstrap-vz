

def validate_manifest(data, validator, error):
	import os.path
	schema_path = os.path.normpath(os.path.join(os.path.dirname(__file__), 'manifest-schema.json'))
	validator(data, schema_path)


def resolve_tasks(tasklist, manifest):
	import tasks
	tasklist.add(tasks.AddUnattendedUpgradesPackage,
	             tasks.EnablePeriodicUpgrades)
