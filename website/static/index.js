function deleteFolder(folderId) {
    fetch("/delete-folder", {
      method: "POST",
      body: JSON.stringify({ folderId: folderId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }