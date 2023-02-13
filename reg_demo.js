const path = require('path');

const ProtocolRegistry = require('protocol-registry');

console.log('Registering...');
// Registers the Protocol
ProtocolRegistry.register({
    protocol: 'testproto', // sets protocol for your command , testproto://**
    command: `start "C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE" `, // $_URL_ will the replaces by the url used to initiate it
    override: true, // Use this with caution as it will destroy all previous Registrations on this protocol
    terminal: true, // Use this to run your command inside a terminal
    script: false
}).then(async () => {
    console.log('Successfully registered');
});