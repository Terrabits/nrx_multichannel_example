from rohdeschwarz.instruments.genericinstrument import GenericInstrument


SMB_ADDRESS   = '172.20.16.226'
ONE_MINUTE_MS = 60 * 1000


# connect to smb
smb = GenericInstrument()
smb.open_tcp(SMB_ADDRESS)
smb.open_log('smb.log')
smb.print_info()

smb.timeout_ms = ONE_MINUTE_MS

# clear errors
smb.write('*CLS')

# preset smb
smb.write('*RST')
smb.query('*OPC?')
assert not smb.errors

# pulse generator
smb.write('SOUR1:PULM:DEL    0 ns')
smb.write('SOUR1:PULM:WIDT 200 us')
smb.write('SOUR1:PULM:PER  400 us')
assert not smb.errors

smb.write('SOUR1:PULM:MODE SING')
assert not smb.errors

smb.write('SOUR1:PULM:STAT ON')
smb.write('SOUR1:PGEN:STAT ON')
smb.write('SOUR1:MOD       ON')
smb.write('OUTP1:STAT      ON')
assert not smb.errors
