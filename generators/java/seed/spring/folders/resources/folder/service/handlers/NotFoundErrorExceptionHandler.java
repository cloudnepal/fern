/**
 * This file was auto-generated by Fern from our API Definition.
 */

package resources.folder.service.handlers;

import java.lang.Object;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import resources.folder.service.exceptions.NotFoundError;

@RestControllerAdvice
public final class NotFoundErrorExceptionHandler {
  @ExceptionHandler(NotFoundError.class)
  ResponseEntity<Object> handle(NotFoundError notFoundError) {
    return new ResponseEntity<>(notFoundError.getBody(), null, NotFoundError.STATUS_CODE);
  }
}