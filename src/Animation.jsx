import React, { useEffect, useState } from 'react';


const images = [
    '/graphics/animations/run_1.png',
    '/graphics/animations/run_2.png',
    '/graphics/animations/run_3.png',
    '/graphics/animations/run_4.png',
    // '/graphics/animations/standing_boi_1.png',
    // '/graphics/animations/standing_boi_2.png',
];


const images2 = [
    '/graphics/animations/standing_boi_2.png',    
    '/graphics/animations/standing_boi_3.png',      
]


const Animation = () => {
    const [currentIndex, setCurrentIndex] = useState(0);


    useEffect(() => {
        console.log('Animation component rendered'); // Check if component is rendering
        const interval = setInterval(() => {
            console.log('Current image:', images[currentIndex]); // Log current image
            setCurrentIndex((prevIndex) => (prevIndex + 1) % images.length);
        }, 200);


        return () => clearInterval(interval);
    }, [currentIndex]);


    return (
        <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', width: '100%' }}>
            <img src={images[currentIndex]} alt="Animation" style={{ display: 'block' }} />
        </div>
    );
};


export default Animation;
