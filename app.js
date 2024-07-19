const express = require('express');
const axios = require('axios');
const schedule = require('node-schedule');
const moment = require('moment-timezone');

const app = express();
const port = 5000;

const tasks = [
    {
        url: "https://tipivid.000webhostapp.com/vidh/tvr.php?id=17252",
        time: "15:35",
        date: "2024-07-20"
    },
    {
        url: "https://tipivid.000webhostapp.com/vidmpd/tv.php?id=17578",
        time: "19:03",
        date: "2024-07-20"
    },
    {
        url: "https://tipivid.000webhostapp.com/vidh/tvr.php?id=17252",
        time: "19:35",
        date: "2024-07-20"
    },
    {
        url: "https://tipivid.000webhostapp.com/vidh/tvr.php?id=17252",
        time: "21:35",
        date: "2024-07-20"
    },

    // Tambahkan tugas lainnya di sini
];

const wib = 'Asia/Jakarta';

const getResponse = async (url) => {
    try {
        const response = await axios.get(url);
        return response.data;
    } catch (error) {
        if (error.response) {
            return `HTTP error occurred: ${error.response.status}`;
        } else {
            return `Other error occurred: ${error.message}`;
        }
    }
};

const job = async (url) => {
    const response = await getResponse(url);
    console.log(`Response from ${url}:\n${response}\n`);
};

const checkAndRunJobs = () => {
    const currentTime = moment().tz(wib).format('HH:mm');
    const currentDate = moment().tz(wib).format('YYYY-MM-DD');
    tasks.forEach((task, index) => {
        if (currentTime === task.time && currentDate === task.date) {
            job(task.url);
            tasks.splice(index, 1);  // Hapus tugas yang sudah dijalankan
        }
    });
    if (tasks.length === 0) {
        schedule.gracefulShutdown();  // Batalkan penjadwalan jika tidak ada tugas lagi
    }
};

schedule.scheduleJob('* * * * *', checkAndRunJobs);

app.get('/', (req, res) => {
    res.json({ message: 'Web service is running. Scheduler is active.' });
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
