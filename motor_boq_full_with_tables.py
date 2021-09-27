locked_rotor_kva = [['A',0,3.15], ['B',3.15,3.55], ['C', 3.55,4], ['D', 4, 4.5], ['E', 4.5, 5], ['F', 5, 5.6], ['G', 5.6, 6.3], ['H', 6.3, 7.1], ['J', 7.1, 8], ['K', 8, 9], ['L', 9, 10], ['M', 10, 11.2], ['N', 11.2, 12.5], ['P', 12.5, 14], ['R', 14, 16], ['S', 16, 18], ['T', 18, 20], ['U', 20, 22.4], ['V', 22.4, 25]];

motor_code_leter_at_full_voltage = [[0,1.25, 'L'], [1.25,2.5, 'K'], [2.5,4,'J'], [4, 6.25,'H'], [6.25,12.5, 'G'], [12.5, 10000, 'F']];
def codeFinder():
	global kva_maximum_locked_rotor_current, kva_minimum_locked_rotor_current, power, code_leter, power_hp;
	for i in motor_code_leter_at_full_voltage:
		power_hp = power*1.34102;
		if(i[1]>power_hp):
			code_leter = i[2];
			break;
	for i in locked_rotor_kva:
		if(i[0] == code_leter):
			kva_maximum_locked_rotor_current = i[2];
			kva_minimum_locked_rotor_current = i[1];


def dataCollector():
	global phase, voltage, power, efficiency, speed, power_factor;
	# phase = float(input('Enter the number of phases "1 or 3"'));
	voltage = float(input('Enter the motors Voltage (415 or 380) '));
	power = float(input('Enter the power rating in Kw'));
	# efficiency = float(input('Enter the efficiency of the motor in % eg 80 '));
	speed = float(input('Enter the motors speed in rpm'));
	# power_factor = float(input('Enter the motors power factor in decimal'));

def torqueAndCurrent():
	global rated_torque_in_Lbft, rated_torque_in_Nm, starting_torque, minimum_locked_rotor_current, maximum_locked_rotor_current, full_load_line_current, full_load_phase_current, starting_current;
	rated_torque_in_Lbft = 5252 * (power/0.75) / speed;
	rated_torque_in_Nm = 9500 * power / speed;
	starting_torque = 3 * rated_torque_in_Nm;
	maximum_locked_rotor_current = 1000 * (power/0.75) * kva_maximum_locked_rotor_current / (1.732 * voltage);
	minimum_locked_rotor_current = 1000 * (power/0.75) * kva_minimum_locked_rotor_current / (1.732 * voltage);
	full_load_line_current = power * 1000 /(1.732 * voltage);
	full_load_phase_current = full_load_line_current/ 1.732;
	starting_current = 7 * full_load_line_current;

def sizeOfFuse():
	global maximum_size_of_time_delay_fuse, maximum_size_of_non_time_delay_fuse;
	maximum_size_of_time_delay_fuse = 3 * full_load_line_current;
	maximum_size_of_non_time_delay_fuse = 1.75 * full_load_line_current;

def sizeOfCircuitBreaker():
	global maximum_size_of_instantaneous_trip_circuit_breaker, maximum_size_of_inverse_trip_circuit_breaker;
	maximum_size_of_instantaneous_trip_circuit_breaker = 8 * full_load_line_current;
	maximum_size_of_inverse_trip_circuit_breaker = 2.5 * full_load_line_current;

def thermalOverloadRelay():
	global minimum_thermal_overload_relay_setting, maximum_thermal_overload_relay_setting, thermal_overload_relay_setting;
	minimum_thermal_overload_relay_setting = 0.7 * full_load_phase_current;
	maximum_thermal_overload_relay_setting = 1.2 * full_load_phase_current;
	thermal_overload_relay_setting = 1 * full_load_line_current;

def sizeAndTypeOfContactor():
	global type_of_contactor, size_of_main_contactor, making_or_breaking_capacity_of_contactor;
	type_of_contactor = "AC3";
	size_of_main_contactor = 1 * full_load_line_current;
	making_or_breaking_capacity_of_contactor = 10 * full_load_line_current;

def results():
	print('*****************************************************************');
	print('Motor power', power,'Kw (', power_hp,'Hp)  NEMA Code: ', code_leter);
	print('Motor rated torque', rated_torque_in_Nm,'Nm');
	print('Motor starting_torque', starting_torque, 'Nm');
	print('Maximum size of time delay fuse: ', maximum_size_of_time_delay_fuse);
	print('Maximum size of non time delay fuse: ', maximum_size_of_non_time_delay_fuse);
	print('Maximum size of instantaneous trip circuit breaker: ', maximum_size_of_instantaneous_trip_circuit_breaker);
	print('Maximum size of inverse trip circuit breaker: ', maximum_size_of_inverse_trip_circuit_breaker);
	print('Maximum thermal overload relay setting: ', maximum_thermal_overload_relay_setting);
	print('Minimum thermal overload relay setting: ', minimum_thermal_overload_relay_setting);
	print('Type of contactor', type_of_contactor);
	print('Size of main contactor', size_of_main_contactor);
	print('Making or breaking capacity of contactor', making_or_breaking_capacity_of_contactor);
	print('*****************************************************************');
	repeater = int(input('Do you want to calculate again 1. For yes 0. For Close'));
	if(repeater):
		caller();

def caller():
	dataCollector();
	codeFinder();
	torqueAndCurrent();
	sizeOfFuse();
	sizeOfCircuitBreaker();
	thermalOverloadRelay();
	sizeAndTypeOfContactor();
	results();

caller();