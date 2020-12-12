export default function appendToEachArrayValue(array, appendString) {
  let arr = array;
  for (let element of arr) {
    element = appendString + element;
  }
  return arr;
}
