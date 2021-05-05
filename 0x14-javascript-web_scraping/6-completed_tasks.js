#!/usr/bin/node
/*
 Javascript that computes the number of tasks completed by user id.

    The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
    Only print users with completed task
    You must use the module request
*/
const url = process.argv[2];
const request = require('request');
const users = {};
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    for (const task of JSON.parse(body)) {
      if (task.completed === true) {
        if (!(task.userId in users)) {
          users[task.userId] = 1;
        } else {
          users[task.userId]++;
        }
      }
    }
    console.log(users);
  }
});
