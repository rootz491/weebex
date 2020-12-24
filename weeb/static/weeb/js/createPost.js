let postWall = document.getElementById('postWall');

let posts = {
    1: {
        user: "sudi",
        caption: 'finally my hard work paid off.',
        img: '{% static "media/degree.jpeg" %}'
    },
    2: {
        user: "karansh491",
        caption: 'Wabalabadubdub',
        img: '{% static "weeb/media/me.jpg" %}'
    },
    3: {
        user: "niku",
        caption: 'Unde repellendus ut neque ipsam molestias soluta eligendi recusandae vel, tempora voluptate! Veritatis, iusto. Illum, illo!',
        img: '{% static "weeb/media/old-rig.jpg" %}'
    },
    4: {
        user: "Sans",
        caption: 'tempora voluptate! Veritatis, iusto. Illum, illo!',
        img: '{% static "weeb/media/sans.png" %}'
    },
    5: {
        user: "Aditya",
        caption: '',
        img: '{% static "weeb/media/whatever.jpeg" %}'
    },
    6: {
        user: "karansh491",
        caption: 'this is final text! get EXCITED you\'ll!',
        img: '{% static "weeb/img/logo.png" %}'
    }
}


let postTemplate = document.getElementsByTagName('template')[0];


for (const [key, data] of Object.entries(posts)) {
// for(const data in posts) {
    console.log(data.user)
    let post = postTemplate.content.cloneNode(true);
    post.querySelector('.user').innerText = data.user;
    post.querySelector('img').src = data.img;
    post.querySelector('.caption').innerText = data.caption;
    postWall.appendChild(post);
}
