from datetime import datetime, timedelta

def validate_conditions(conditions):
	counter = 0
	for condition in conditions:
		if not condition.get('hours'):
			counter += 1
		if condition.get('hours', 0) > 24:
			raise ValueError('Hours cannot be > 24')
	if counter != 1:
		raise ValueError('Invalid conditions')


# Ensure all condititons have hours
def ensure_conditions(conditions):
	for condition in conditions: # condition = {'hours': 10, 'percent': 10}
		if not condition.get('hours'):
			condition['hours'] = 0
#	return conditions


def sort_conditions(conditions):
	sorted_conditions = sorted(conditions, key=lambda c: c['hours'], reverse = True)
	return sorted_conditions

# interval = [[24,12), [12,6), [6,0)]
def pair_conditions(conditions):
	interval = []
	for i in range(len(conditions) - 1):
		interval.append((conditions[i]['hours'], conditions[i + 1]['hours']))
	return interval

def current_condition(conditions, start, now):
	return conditions[0]

def get_cancellation_fee(price, percent):
	return price * (percent / 100)		

def get_cancellation_policy(conditions, price, start, now):
	assert start < now, "Error"
	validate_conditions(conditions)
	ensured_conditions = ensure_conditions(condititons)
	
	if (len(ensured_conditions) == 1):
		return ensured_conditions[0]['percent']

	sorted_conditions = sort_conditions(ensured_conditions)
	group_conditions = group_conditions(sorted_conditions)
	current = current_condition(group_conditions)
	
	return get_cancellation_fee(current)

def main():
	now = datetime.now()
	booking_start = now + timedelta(hours = 10)
	price = 1000
	conditions = [
		{ 'hours': 24, 'percent': 10 }, 
		{ 'hours': 12, 'percent': 50 }, 
		{ 'hours': 6, 'percent': 80 }, 
		{ 'percent': 100 } # default
		]
	condititons = ensure_conditions(conditions)
	group_conditions(conditions)
	# get_cancellation_policy(conditions, price, booking_start, now)

if __name__ == '__main__':
	main()