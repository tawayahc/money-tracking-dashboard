def get_styles():
    """Return the CSS styles as a string."""
    return """
    <style>
    .scroll-container {
        display: grid;
        grid-template-rows: repeat(2, 1fr);
        grid-auto-flow: column; 
        grid-auto-columns: minmax(150px, 1fr); 
        gap: 10px;
        overflow-x: auto; 
        overflow-y: hidden; 
        padding: 0px;
        white-space: nowrap; 
        max-width: 100%;
    }
    .scroll-container > div {
        display: flex;
        justify-content: center;
        align-items: center;
        min-width: 150px; 
        min-height: 100px; 
        text-align: center; 
        border: 1px solid #ddd; 
        border-radius: 5px; 
        background-color: white;
        box-sizing: border-box;
        overflow: hidden;
        word-wrap: break-word;
        padding: 10px;
    }
    .scroll-container > div span {
        display: inline-block;
        max-width: 100%;
        text-overflow: ellipsis;
        white-space: normal; 
        font-size: 14px; 
        word-break: break-word; 
        overflow-wrap: break-word; 
    }
    </style>
    """
