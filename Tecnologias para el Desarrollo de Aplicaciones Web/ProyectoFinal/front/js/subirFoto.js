$(document).readey(function(){
    
    function subeFoto( informacion, actionUrl ) {
        const storage = getStorage();
        const imageRef = ref(storage, 'images/' + file.name);
        uploadBytesResumable(imageRef, file)
          .then((snapshot) => {
            console.log('Uploaded', snapshot.totalBytes, 'bytes.');
            console.log('File metadata:', snapshot.metadata);
            // Let's get a download URL for the file.
            getDownloadURL(snapshot.ref).then((url) => {
              console.log('File available at', url);
              // ...
            });
          }).catch((error) => {
            console.error('Upload failed', error);
            // ...
          });
    }

});