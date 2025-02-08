import React, { useEffect, useState } from 'react';

const runningImages = [
    '/graphics/animations/run_1.png',
    '/graphics/animations/run_2.png',
    '/graphics/animations/run_3.png',
    '/graphics/animations/run_4.png',
];

const standingImages = [
    '/graphics/animations/standing_boi_2.png',    
    '/graphics/animations/standing_boi_3.png',      
];

const Animation = ({ isRunning }) => {
    const [currentIndex, setCurrentIndex] = useState(0);
    const images = isRunning ? runningImages : standingImages; // choosing running vs standing

    useEffect(() => {
        // reset animation frame when switching between running and standing
        setCurrentIndex(0);
    }, [isRunning]);

    useEffect(() => {
        const interval = setInterval(() => {
            setCurrentIndex((prevIndex) => (prevIndex + 1) % images.length);
        }, 200);

        return () => clearInterval(interval);
    }, [images.length, currentIndex]);

    return (
        <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', width: '100%' }}>
            {images.length > 0 && (
                <img src={images[currentIndex]} alt="Animation" style={{ display: 'block' }} />
            )}
        </div>
    );
};

export default Animation;
