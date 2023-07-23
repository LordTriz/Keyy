from licensing.models import *
from licensing.methods import Key, Helpers

RSAPubKey = "<RSAKeyValue><Modulus>qUQPJ+I0Wv/m6yqPDwZJ6MAIrKsm2h9gxPIpx9jnVKDsrXMANNIodqHhX84uWhBc1lUxF3XqFzkKU7J4hJwZl0Tbwncu3lgoPMLAQ2xE48KuFLbVBMyMw7zjrNGDCFWF12oaNeiJQoAgvviEY0jEhoFUfDy/K0RMq6vMI6iKc7S8CS7yVmWTIHs+NKrr4f3uQsZieRmC5eh03k51OVTv8dMTB9NYtFqp8pFe2KNXIkDQI/tn4oDUkQt1d+mxsrxDQ8xG8zBxPTS7jIRdTChdVCJbSYqmeD2VkYZoc3gmTO7GA54HvhxGOEB6DAsutgTxeGanC36afZAEt5rq8/Wh9Q==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>"#ENTER RSAKEY
auth = "WyI1NTI4MDYwMSIsInNlZmFSeVNxaENHMW5uMm9FQjR1dGdhdUplbHMxZXRjVksrMjkxbHkiXQ==" ## AUTHKEY WITH ACTIVATE !
def Authkey():
    key = str(input(" Enter Auth Key :-"))
    result = Key.activate(token=auth,\
        rsa_pub_key=RSAPubKey,\
        product_id='21050', \
        key=key,\
        machine_code=Helpers.GetMachineCode())

    if result[0] == None or not Helpers.IsOnRightMachine(result[0]):
    # an error occurred or the key is invalid or it cannot be activated
    # (eg. the limit of activated devices was achieved)
        print("The license does not work: {0}".format(result[1]))
    else:
    # everything went fine if we are here!
        print("The license is valid!")
        pass
Authkey()