const Discord = require('discord.js');
const client = new Discord.Client();

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.on('message', msg => {
    console.log('pong')
});

client.login('NzYyMDk4Nzk2NzQ1NzE5ODA5.X3kN0A.cT4KBdUEle6FXPUs4MqljSSxT4I');