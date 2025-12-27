<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Burn & Wound Detection</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/引入/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Poppins', sans-serif;
            /* صورة خلفية طبية هادئة */
            background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), 
                        url('https://images.unsplash.com/photo-1576091160550-2173dba999ef?ixlib=rb-4.0.3&auto=format&fit=crop&w=2070&q=80');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0;
        }

        .glass-card {
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(15px);
            -webkit-backdrop-filter: blur(15px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
            color: white;
            max-width: 600px;
            width: 90%;
            text-align: center;
        }

        .main-title {
            font-weight: 700;
            font-size: 2.5rem;
            margin-bottom: 20px;
            background: linear-gradient(to right, #00f2fe, #4facfe);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .upload-section {
            border: 2px dashed rgba(255, 255, 255, 0.5);
            border-radius: 15px;
            padding: 30px;
            margin-top: 30px;
            transition: all 0.3s ease;
            cursor: pointer;
        }

        .upload-section:hover {
            background: rgba(255, 255, 255, 0.1);
            border-color: #00f2fe;
        }

        .btn-detect {
            background: linear-gradient(to right, #4facfe 0%, #00f2fe 100%);
            border: none;
            padding: 12px 35px;
            border-radius: 50px;
            font-weight: 600;
            margin-top: 25px;
            transition: transform 0.2s;
        }

        .btn-detect:hover {
            transform: scale(1.05);
            box-shadow: 0 5px 15px rgba(79, 172, 254, 0.4);
        }

        #imagePreview {
            max-width: 100%;
            border-radius: 10px;
            margin-top: 20px;
            display: none;
        }
    </style>
</head>
<body>

<div class="glass-card">
    <h1 class="main-title">Burn & Wound Detection</h1>
    <p class="lead">Using Advanced Deep Learning Technology</p>
    
    <div class="upload-section" onclick="document.getElementById('fileInput').click()">
        <i class="bi bi-cloud-arrow-up fs-1"></i>
        <h5>Drag & Drop or Click to Upload Image</h5>
        <input type="file" id="fileInput" hidden accept="image/*" onchange="previewImage(event)">
        <img id="imagePreview" alt="Image Preview">
    </div>

    <button class="btn btn-primary btn-detect">Start Analysis</button>
</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css">

<script>
    function previewImage(event) {
        const reader = new FileReader();
        const imagePreview = document.getElementById('imagePreview');
        
        reader.onload = function() {
            if (reader.readyState === 2) {
                imagePreview.src = reader.result;
                imagePreview.style.display = 'block';
            }
        }
        reader.readAsDataURL(event.target.files[0]);
    }
</script>

</body>
</html>