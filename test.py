import React, { useState } from 'react';

const ImageUploader = () => {
  const [preview, setPreview] = useState(null);

  // Handle file upload and generate image preview
  const handleImageUpload = (event) => {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onloadend = () => {
        setPreview(reader.result);
      };
      reader.readAsDataURL(file);
    }
  };

  return (
    <div style={{ textAlign: 'center', marginTop: '2rem' }}>
      {/* Phase 1.1: Upload button */}
      <input type="file" accept="image/*" onChange={handleImageUpload} />
      
      {/* Phase 1.2: Image preview */}
      {preview && (
        <div style={{ marginTop: '1rem' }}>
          <h3>Image Preview:</h3>
          <img src={preview} alt="Uploaded preview" style={{ maxWidth: '300px', border: '1px solid #ccc' }} />
        </div>
      )}
    </div>
  );
};

export default ImageUploader;
