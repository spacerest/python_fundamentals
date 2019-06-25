'''

If a runner runs 10 miles in 30 minites and 30 seconds,
What is his/her average speed in kilometers per hour? (Tip: 1 mile = 1.6 km)

'''

miles_in_km = 10 * 1.6
sec_per_hour = 3600
run_time_in_sec = 30 * 60 + 30

# x km / hr = (convert miles to km) / (convert runtime to hrs)
#x km  / hr = (10 * 1.6) km / (30.5 / 60) hr
print((miles_in_km / (run_time_in_sec / sec_per_hour)))