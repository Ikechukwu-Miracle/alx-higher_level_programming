#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const tasksData = JSON.parse(body);
    const completedTasks = tasksData.filter(task => task.completed);
    const completedTasksByUser = completedTasks.reduce((acc, task) => {
      const userId = task.userId.toString();
      acc[userId] = (acc[userId] || 0) + 1;
      return acc;
    }, {});
    console.log(completedTasksByUser);
  }
});
