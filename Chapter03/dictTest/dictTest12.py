signals = {
    'green' : 'go',
    'yellow' : 'go faster',
    'red' : 'smile for the camera',
}

save_signals = signals
signals['blue'] = 'confuse everyone'
print(save_signals)

signals = {
    'green' : 'go',
    'yellow' : 'go faster',
    'red' : 'smile for the camera',
}

save_signals = signals.copy()
signals['blue'] = 'confuse everyone'
print('signals : ' + repr(signals))
print('save_signals : ' + str(save_signals))