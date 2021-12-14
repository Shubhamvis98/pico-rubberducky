import storage

# CONFIG
ENABLE_USB = True
RW_ACCESS = True

# FUNCTIONS
print('\n\n')

if ENABLE_USB:
    print('USB Drive: Enabled')
else:
    print('USB Drive: Disabled')
    storage.disable_usb_drive()

if RW_ACCESS:
    print('Mount: Read-Write')
    storage.remount('/', False)
else:
    print('Mount: Read-Only')
    storage.remount('/', True)
