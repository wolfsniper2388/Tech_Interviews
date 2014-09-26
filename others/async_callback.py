''' Assume in a system, users will register a callback function with system and that callback function will be called when an event is triggered
    but if the event is already triggered, the user will synchronously call the callback function
    For example
    suppose user i registers cb i at time Ti,
    and the event happens at time Te
    and assume that T1 < T2 < T3 <...< Tm < Te < Tm+1 < ... < Tn
    at time Te, cb1..cbm will be called
    cbm+1 .. cbn will be called synchronously
    implement two APIs: void register_cb (cb), and void event_trigger() 
'''

is_triggered = 0
def register_cb(cb):
    q=deque([])
    lock()
    is_triggered = 0
    if is_triggered == 0:
        q.append(cb)
        unlock()
    else:
        unlock()
        cb()

def trigger_event():
    is_triggered = 1
    lock()
    unlock()
    while q:
        q.popleft()
        cb()
        