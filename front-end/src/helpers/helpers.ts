/**
 * Verifica si un objeto está vacío. Esta es una función auxiliar para ` Object. keys (). length
 *
 * Args:
 * 	 obj: El objeto a comprobar debe ser un objeto.
 * 	 object: El objeto que quiero comprobar debe ser un objeto.
 *
 * Returns:
 * 	 { boolean } Verdadero si el objeto está vacío y falso si no lo está
 */
export function isEmpty(obj: object): boolean {
    return Object.entries(obj).length === 0;
  }