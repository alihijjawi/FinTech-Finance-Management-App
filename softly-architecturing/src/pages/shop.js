import React from 'react';
import { useState } from "react";
import "../static/css/shop.css"
import image_1 from "../static/images/Capture.PNG"
import image_2 from "../static/images/minion1.jpg"
import image_3 from "../static/images/minion2.jpg"
const Shop = () => {
	return (
        <div>
        <div class="row" >
            <div class="block">
                <div class="card">
                <img class = "img" src={image_2} alt="SHREK" width = "100%"/>
                <h2 class = "name">Rare Minion</h2>
                <p class="price">$400.00</p>
                <p class = "name">A Rare Avatar Icon</p>
                <p><button class = "buy-button">Buy</button></p>
                </div>
            </div>

            <div class="block">
            <div class="card">
                <img class = "img" src={image_1} alt="SHREK" width = "100%"/>
                <h2 class = "name">Rare Shrek</h2>
                <p class="price">$4000.00</p>
                <p class = "name">A Rare Avatar Icon</p>
                <p><button class = "buy-button">Buy</button></p>
                </div>
            </div>

            <div class="block">
            <div class="card">
                <img class = "img" src={image_3} alt="SHREK" width = "100%"/>
                <h2 class = "name">Rare Minion</h2>
                <p class="price">$500.00</p>
                <p class = "name">A Rare Avatar Icon</p>
                <p><button class = "buy-button">Buy</button></p>
                </div>
            </div>
           
            
       
        </div>

        <div>
            <p><button class = "button">Back</button></p>
        </div>
        
        </div>

        
		
	);
};

export default Shop;
