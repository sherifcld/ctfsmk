const express = require('express');
const app = express();
app.use(express.json());

function merge(target, source) {
    for (let key in source) {
        if (key === '__proto__' || key === 'constructor') continue;
        if (typeof target[key] === 'object' && typeof source[key] === 'object') {
            merge(target[key], source[key]);
        } else {
            target[key] = source[key];
        }
    }
}

app.post('/update-profile', (req, res) => {
    let profile = { name: 'guest', role: 'user' };
    merge(profile, req.body);
    res.json({ message: 'Profile updated!', profile: profile });
});

app.get('/debug', (req, res) => {
    // If polluted, this could lead to RCE or other issues
    res.json({ status: 'ok' });
});

app.listen(3000, () => {
    console.log('Server running on port 3000');
});
