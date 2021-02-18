from rohdeschwarz.instruments.genericinstrument import GenericInstrument

# Assumes pulsed RF into NRX
# Channel B (2) and Channel E (5).

NRX_ADDRESS   = '172.20.16.253'
ONE_MINUTE_MS = 60 * 1000


# connect to nrx
nrx = GenericInstrument()
nrx.open_tcp(NRX_ADDRESS)
nrx.open_log('nrx.log')
nrx.print_info()

nrx.timeout_ms = ONE_MINUTE_MS

# clear previous errors
nrx.write('*CLS')

# start from preset
nrx.write('*RST')
nrx.query('*OPC?')
assert not nrx.errors

# display two diagrams
nrx.write('DISP:LAY L2')

# diagram 1: channel B (2)
nrx.write('SENS2:FREQ 1 GHz')
nrx.write('CALC1:CHAN1:SENS:IND 2')
nrx.write('CALC1:TYPE TGAT')
nrx.write('CALC1:TGAT:SEL 1')
nrx.write('CALC1:TGAT1:OFFS   0 us')
nrx.write('CALC1:TGAT1:TIME 200 us')
nrx.write('TRIG1:LEV -39.999 dBm')
assert not nrx.errors

# diagram 2: channel E (5)
nrx.write('SENS5:FREQ 1 GHz')
nrx.write('CALC2:CHAN1:SENS:IND 5')
nrx.write('CALC2:TYPE TGAT')
nrx.write('CALC2:TGAT:SEL 1')
nrx.write('CALC2:TGAT1:OFFS   0 us')
nrx.write('CALC2:TGAT1:TIME 200 us')
nrx.write('TRIG2:LEV -39.999 dBm')
assert not nrx.errors

# single sweep mode
nrx.write('INIT:ALL:CONT OFF')


# measure all channels
nrx.write('INIT:ALL')
assert not nrx.errors

# operation complete?
nrx.query('*OPC?')
assert not nrx.errors

# read channel B
channel_b = float(nrx.query('CALC1:DATA?'))
assert not nrx.errors

# read channel E
channel_e = float(nrx.query('CALC2:DATA?'))
assert not nrx.errors

# results
print(f'channel_b={channel_b}')
print(f'channel_e={channel_e}')
