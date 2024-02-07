#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error || response.statusCode !== 200) {
    console.error('Error making the request');
    return;
  }

  const todosData = JSON.parse(body);
  const completedTasksByUser = {};

  todosData.forEach(todo => {
    if (todo.completed) {
      completedTasksByUser[todo.userId] = (completedTasksByUser[todo.userId] || 0) + 1;
    }
  });

  console.log('{');
  Object.keys(completedTasksByUser).forEach((userId, index, array) => {
    const comma = index < array.length - 1 ? ',' : '';
    console.log(`  '${userId}': ${completedTasksByUser[userId]}${comma}`);
  });
  console.log('}');
});
