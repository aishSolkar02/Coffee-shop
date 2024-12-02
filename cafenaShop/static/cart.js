function updateQuantity(operation,serviceId)
{
   const inputBox=document.getElementById("quantity"+serviceId);
   inputBox.value=parseInt(inputBox.value)+operation;
}