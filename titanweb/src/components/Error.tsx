type ErrorProps = {
    error: string;
    onDismiss: () => void;
  };
  
  export function Error({ error, onDismiss }: ErrorProps) {
    return (
      <div>
        {error && (
          <div className="error-message">
            {error}
            <button onClick={onDismiss} className="dismiss-error-btn">
              X
            </button>
          </div>
        )}
      </div>
    );
  }