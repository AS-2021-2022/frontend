<script>
import { afterUpdate } from "svelte";
import {token , email} from "./stores/store.js";
import {callAPI} from "./global.js";
import { get } from "svelte/store";

    export let userid;
    var messages = [];
    var last_id = -1;
    
    afterUpdate(() => {

        if(last_id != userid)
        {
            messages = [];
            getMessages(0 , 30);
            last_id = userid;
        }
        
    });


    async function getMessages(depth , n)
    {
        var dict = {"token" : get(token), "targetID" : userid, "depth" : depth , "n" : n};

        let awnser = await callAPI("contactMessages" , dict);

        console.log(awnser);

        if(awnser["status"] == "accepted")
        {

            for(let i = 0;i < Object.keys(awnser["messages"]).length;i++)
            {
                messages.push(awnser["messages"][i-depth]);
            }
            messages = messages;
        }
        //console.log(messages);
    }



    async function sendMessage()
    {
        var h = document.getElementById("message-box");
        let text = h.value;
        if(text != "")
        {
            
            h.value = "sending ...";
            
           let awnser = await callAPI("sendMessage" , {"token" : get(token) , "targetID" : userid , "message" : text});
                   
            if(awnser["status"] == "accepted")
            {
                messages = [...messages , {"origin" : "you" , "text" : text}];
                h.value = "";
            }
            if(awnser["status"] == "rejected")
            {
                console.log("message rejected");
            }
           
        }
        
    }

</script>

<main>
    <div style = "overflow:auto; opacity:1.0;">
        {#each messages as message}
        <div class = "message">
            {#if message["origin"] === get(email) || message["origin"] == "you"}
            
            <div class = "messageRight">{message.text}</div>
            {:else}

                <div class = "messageLeft">
                    
                    {message.text}
                    <div class = "messageOrigin">{message.origin}</div>

                </div>
            
            {/if}
        </div>
        {/each}
    </div>

    <div class = "message-box">
        <textarea id = "message-box" type = "text" class = "message-input" placeholder = "Type message..."></textarea>
        <button class = "message-send" on:click={() => {sendMessage()}}>SEND</button>
    </div>
</main>

<style>
    main
    {
        background-color: #e5e5f7;
        
        width: 100%;
        display: flex;
        flex-direction: column;
        height:100%;
        overflow:visible;
    }

    .messageLeft
    {
        width: fit-content;
        background-color: #f1f1f1f1;
        max-width: 70%;
        margin-left: 50px;
        margin-top: 10px;
        margin-bottom: 10px;
        padding-left:20px;
        padding-right: 20px;
        border-radius: 20px;
        font-size: 24px;
        float:left;
        height:fit-content;
        clear:both;
        text-align: left;
        color:black;
        overflow-wrap: anywhere;
    }

    .messageOrigin
    {
        border-top:2px solid rgb(232, 232, 232);
        text-align:left;
        font-size:18px;
    }

    .messageRight
    {
        width: fit-content;
        max-width: 70%;
        height:fit-content;
        margin-right:50px;
        margin-top: 10px;
        margin-bottom: 10px;
        padding-left:20px;
        padding-right: 20px;
        border-radius: 20px;
        background-color: rgb(58,132,255);
        float: right;
        font-size: 24px;
        text-align: right;
        color:white;
        clear:both;
        overflow-wrap: anywhere;
    }

    .message-box {
    width: 90%;
    background: #fff; 
    margin:2px auto;

    margin-top: auto;
    display:flex;
    

    -webkit-border-radius: 20px;
    -moz-border-radius: 20px;
    border-radius: 20px; 
    
    border:1px solid #ccc;
    
    }

    .message-input {
    background: none;
    float:left;
    border: none;
    resize: none; 
    outline:none;
    /* color: rgba(255, 255, 255, .8);*/
    font-size: 24px;
    height: 50px;
    margin: 0;

    width: 90%;
    color: #444;
    overflow:hidden;
    }

    .message-send
    {
        height:50px;
        width:10%;
        background-color: #f1f1f1f1;
        border:none;
        color:rgb(58, 58, 213);
        outline:none;
        transition-duration: 0.3s;
        border-top-right-radius: 20px;
        border-bottom-right-radius: 20px;
    }

    .message-send:hover
    {
        background-color: rgb(58,132,255);
        color:white;
        transition-duration: 0.3s;
        border-top-right-radius: 20px;
        border-bottom-right-radius: 20px;
    }

    .message
    {
        
    }
</style>